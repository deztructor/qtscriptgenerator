#!/usr/bin/python

import re
import sys

pkg_tpl = '''
%package -n qtscriptbindings@@suffix@@-{name}
Summary: Qt {name} bindings for Qt Script
Requires: qtscriptbindings@@suffix@@-common = %{{version}}-%{{release}}
Group: System Environment/Libraries
%{{?_qt:Requires: qt%{{?_isa}} >= %{{my_qt_ver}}}}
%description -n qtscriptbindings@@suffix@@-{name}
Bindings providing access to {name} portions of the Qt API
from within Qt Script.'''

file_tpl='''
%files -n qtscriptbindings@@suffix@@-{name}
%{{_qt@@ver@@_plugindir}}/script/libqtscript_{name}.so*'''

packages = ['core', 'gui', 'network', 'opengl', 'sql', 'svg', 'uitools',
            'webkit', 'xml', 'xmlpatterns']

deps_qt4 = '''
# phonon bindings currently busted, see no_phonon patch
#BuildRequires: pkgconfig(phonon)
BuildRequires: pkgconfig(QtCore)
BuildRequires: pkgconfig(QtGui)
BuildRequires: pkgconfig(QtNetwork)
BuildRequires: pkgconfig(QtOpenGL)
BuildRequires: pkgconfig(QtSql)
BuildRequires: pkgconfig(QtSvg)
BuildRequires: pkgconfig(QtUiTools)
BuildRequires: pkgconfig(QtWebKit)
BuildRequires: pkgconfig(QtXml)
BuildRequires: pkgconfig(QtXmlPatterns)
'''
deps_qt5 = '''
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5OpenGL)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5UiTools)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5WebKitWidgets)
#BuildRequires: pkgconfig(Qt5V8)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5XmlPatterns)
'''

deps = { 'qt4' : deps_qt4
          , 'qt5' : deps_qt5
          }

specs = { 'qt4' : 'qtscriptgenerator.{}'
          , 'qt5' : 'qtscriptgenerator-qt5.{}'
          }

def generate(lib) :
    dep = deps[lib]
    spec = specs[lib]

    pkg_templates = { 'files' : file_tpl, 'pkgs' : pkg_tpl }
    templates = { 'deps' : dep
                  , 'ver' : '5' if lib == 'qt5' else ''
                  , 'suffix' : '-' + lib if lib == 'qt5' else '' }

    def replaced(l):
        global packages
        m = re.match(r'.*@@([a-z]+)@@.*', l)
        if m is None:
            return (l,)
        name = m.group(1)
        if name in pkg_templates:
            lines = '\n'.join([pkg_templates[name].format(name = x) for x in packages])
        elif name in templates:
            lines = l.replace('@@{}@@'.format(name), templates[name])
        return lines.split('\n')



    import itertools

    with open('qtscriptgenerator.spec.tpl') as f:
        #lines = [x.strip() for x in f.readlines()]
        lines = f.readlines()
        res = itertools.chain(*[replaced(l.strip()) for l in lines])
        res = list(itertools.chain(*[replaced(l) for l in res]))
        with open(spec.format('spec'), 'w') as f:
            f.write('\n'.join(res))
            f.write('\n')

[generate(l) for l in ['qt4', 'qt5']]
