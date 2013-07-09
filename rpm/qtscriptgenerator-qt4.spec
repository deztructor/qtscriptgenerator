Name:    qtscriptgenerator-qt4
Summary: A tool to generate Qt bindings for Qt Script
Version: 0.0.0
Release: 0

License: GPLv2
Group:	 System Environment/Libraries
URL:     http://github.com/deztructor/qtscriptgenerator
Source0: %{name}-%{version}.tar.bz2
Source1: qtscriptgenerator.spec.tpl
Source2: generate-spec.py
#BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

# explictly BR libxslt, for xsltproc
BuildRequires: libxslt
BuildRequires: gdb
Provides: qtscriptgenerator = %{version}
Obsoletes: qtscriptgenerator < 0.2.7

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


%define my_qt_ver %{_qt_version}

# not strictly required, but the expectation would be for the
# bindings to be present
Requires: qtscriptbindings-qt4-common = %{version}-%{release}

%description
Qt Script Generator is a tool to generate Qt bindings for Qt Script.

%package -n qtscriptbindings-qt4-common
Summary: Qt bindings for Qt Script - common files
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
Provides: qtscriptbindings-common = %{version}
Obsoletes: qtscriptbindings-common < 0.2.7
%description -n qtscriptbindings-qt4-common
Common files for QtScript Qt bindings packages.

%package -n qtscriptbindings-qt4-doc
Summary: Qt bindings for Qt Script - documentation and examples
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
Provides: qtscriptbindings-doc = %{version}
Obsoletes: qtscriptbindings-doc < 0.2.7
%description -n qtscriptbindings-qt4-doc
Examples and documentation for QtScript Qt bindings


%package -n qtscriptbindings-qt4-core
Summary: Qt core bindings for Qt Script
Requires: qtscriptbindings-qt4-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-core = %{version}
Obsoletes: qtscriptbindings-core < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt4-core
Bindings providing access to core portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt4-gui
Summary: Qt gui bindings for Qt Script
Requires: qtscriptbindings-qt4-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-gui = %{version}
Obsoletes: qtscriptbindings-gui < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt4-gui
Bindings providing access to gui portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt4-network
Summary: Qt network bindings for Qt Script
Requires: qtscriptbindings-qt4-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-network = %{version}
Obsoletes: qtscriptbindings-network < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt4-network
Bindings providing access to network portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt4-opengl
Summary: Qt opengl bindings for Qt Script
Requires: qtscriptbindings-qt4-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-opengl = %{version}
Obsoletes: qtscriptbindings-opengl < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt4-opengl
Bindings providing access to opengl portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt4-sql
Summary: Qt sql bindings for Qt Script
Requires: qtscriptbindings-qt4-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-sql = %{version}
Obsoletes: qtscriptbindings-sql < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt4-sql
Bindings providing access to sql portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt4-svg
Summary: Qt svg bindings for Qt Script
Requires: qtscriptbindings-qt4-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-svg = %{version}
Obsoletes: qtscriptbindings-svg < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt4-svg
Bindings providing access to svg portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt4-uitools
Summary: Qt uitools bindings for Qt Script
Requires: qtscriptbindings-qt4-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-uitools = %{version}
Obsoletes: qtscriptbindings-uitools < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt4-uitools
Bindings providing access to uitools portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt4-webkit
Summary: Qt webkit bindings for Qt Script
Requires: qtscriptbindings-qt4-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-webkit = %{version}
Obsoletes: qtscriptbindings-webkit < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt4-webkit
Bindings providing access to webkit portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt4-xml
Summary: Qt xml bindings for Qt Script
Requires: qtscriptbindings-qt4-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-xml = %{version}
Obsoletes: qtscriptbindings-xml < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt4-xml
Bindings providing access to xml portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt4-xmlpatterns
Summary: Qt xmlpatterns bindings for Qt Script
Requires: qtscriptbindings-qt4-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-xmlpatterns = %{version}
Obsoletes: qtscriptbindings-xmlpatterns < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt4-xmlpatterns
Bindings providing access to xmlpatterns portions of the Qt API
from within Qt Script.

%prep
%setup -q -n %{name}-%{version}

%build

# workaround buildsys bogosity, see also:
# http://code.google.com/p/qtscriptgenerator/issues/detail?id=38
export INCLUDE=/usr/include

export QTDIR=%{_qt_headerdir}

pushd generator
%qmake
make %{?jobs:-j%jobs}
./generator --include-paths=%{_qt_headerdir}
popd

pushd qtbindings
%qmake
make %{?jobs:-j%jobs}
popd

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_qt_plugindir}/script/
# install doesn't do symlinks
cp -a plugins/script/libqtscript* \
%{buildroot}%{_qt_plugindir}/script/

install -D -p -m755 generator/generator %{buildroot}%{_qt_bindir}/qtbindings-generator

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_qt_bindir}/qtbindings-generator

%files -n qtscriptbindings-qt4-common
%defattr(-,root,root,-)
%doc README
%doc LICENSE.LGPL LGPL_EXCEPTION.txt

%files -n qtscriptbindings-qt4-doc
%defattr(-,root,root,-)
%doc doc/
%doc examples/


%files -n qtscriptbindings-qt4-core
%{_qt_plugindir}/script/libqtscript_core.so*

%files -n qtscriptbindings-qt4-gui
%{_qt_plugindir}/script/libqtscript_gui.so*

%files -n qtscriptbindings-qt4-network
%{_qt_plugindir}/script/libqtscript_network.so*

%files -n qtscriptbindings-qt4-opengl
%{_qt_plugindir}/script/libqtscript_opengl.so*

%files -n qtscriptbindings-qt4-sql
%{_qt_plugindir}/script/libqtscript_sql.so*

%files -n qtscriptbindings-qt4-svg
%{_qt_plugindir}/script/libqtscript_svg.so*

%files -n qtscriptbindings-qt4-uitools
%{_qt_plugindir}/script/libqtscript_uitools.so*

%files -n qtscriptbindings-qt4-webkit
%{_qt_plugindir}/script/libqtscript_webkit.so*

%files -n qtscriptbindings-qt4-xml
%{_qt_plugindir}/script/libqtscript_xml.so*

%files -n qtscriptbindings-qt4-xmlpatterns
%{_qt_plugindir}/script/libqtscript_xmlpatterns.so*
