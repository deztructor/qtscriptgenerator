Name:    qtscriptgenerator-qt5
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


%define my_qt_ver %{_qt5_version}

# not strictly required, but the expectation would be for the
# bindings to be present
Requires: qtscriptbindings-qt5-common = %{version}-%{release}

%description
Qt Script Generator is a tool to generate Qt bindings for Qt Script.

%package -n qtscriptbindings-qt5-common
Summary: Qt bindings for Qt Script - common files
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
Provides: qtscriptbindings-common = %{version}
Obsoletes: qtscriptbindings-common < 0.2.7
%description -n qtscriptbindings-qt5-common
Common files for QtScript Qt bindings packages.

%package -n qtscriptbindings-qt5-doc
Summary: Qt bindings for Qt Script - documentation and examples
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
Provides: qtscriptbindings-doc = %{version}
Obsoletes: qtscriptbindings-doc < 0.2.7
%description -n qtscriptbindings-qt5-doc
Examples and documentation for QtScript Qt bindings


%package -n qtscriptbindings-qt5-core
Summary: Qt core bindings for Qt Script
Requires: qtscriptbindings-qt5-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-core = %{version}
Obsoletes: qtscriptbindings-core < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt5-core
Bindings providing access to core portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt5-gui
Summary: Qt gui bindings for Qt Script
Requires: qtscriptbindings-qt5-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-gui = %{version}
Obsoletes: qtscriptbindings-gui < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt5-gui
Bindings providing access to gui portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt5-network
Summary: Qt network bindings for Qt Script
Requires: qtscriptbindings-qt5-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-network = %{version}
Obsoletes: qtscriptbindings-network < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt5-network
Bindings providing access to network portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt5-opengl
Summary: Qt opengl bindings for Qt Script
Requires: qtscriptbindings-qt5-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-opengl = %{version}
Obsoletes: qtscriptbindings-opengl < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt5-opengl
Bindings providing access to opengl portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt5-sql
Summary: Qt sql bindings for Qt Script
Requires: qtscriptbindings-qt5-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-sql = %{version}
Obsoletes: qtscriptbindings-sql < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt5-sql
Bindings providing access to sql portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt5-svg
Summary: Qt svg bindings for Qt Script
Requires: qtscriptbindings-qt5-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-svg = %{version}
Obsoletes: qtscriptbindings-svg < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt5-svg
Bindings providing access to svg portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt5-uitools
Summary: Qt uitools bindings for Qt Script
Requires: qtscriptbindings-qt5-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-uitools = %{version}
Obsoletes: qtscriptbindings-uitools < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt5-uitools
Bindings providing access to uitools portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt5-webkit
Summary: Qt webkit bindings for Qt Script
Requires: qtscriptbindings-qt5-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-webkit = %{version}
Obsoletes: qtscriptbindings-webkit < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt5-webkit
Bindings providing access to webkit portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt5-xml
Summary: Qt xml bindings for Qt Script
Requires: qtscriptbindings-qt5-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-xml = %{version}
Obsoletes: qtscriptbindings-xml < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt5-xml
Bindings providing access to xml portions of the Qt API
from within Qt Script.

%package -n qtscriptbindings-qt5-xmlpatterns
Summary: Qt xmlpatterns bindings for Qt Script
Requires: qtscriptbindings-qt5-common = %{version}-%{release}
# for javascript packages independent on qt version
Provides: qtscriptbindings-xmlpatterns = %{version}
Obsoletes: qtscriptbindings-xmlpatterns < 0.2.7
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings-qt5-xmlpatterns
Bindings providing access to xmlpatterns portions of the Qt API
from within Qt Script.

%prep
%setup -q -n %{name}-%{version}

%build

# workaround buildsys bogosity, see also:
# http://code.google.com/p/qtscriptgenerator/issues/detail?id=38
export INCLUDE=/usr/include

export QTDIR=%{_qt5_headerdir}

pushd generator
%qmake5
make %{?jobs:-j%jobs}
./generator --include-paths=%{_qt5_headerdir}
popd

pushd qtbindings
%qmake5
make %{?jobs:-j%jobs}
popd

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_qt5_plugindir}/script/
# install doesn't do symlinks
cp -a plugins/script/libqtscript* \
%{buildroot}%{_qt5_plugindir}/script/

install -D -p -m755 generator/generator %{buildroot}%{_qt5_bindir}/qtbindings-generator

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_qt5_bindir}/qtbindings-generator

%files -n qtscriptbindings-qt5-common
%defattr(-,root,root,-)
%doc README
%doc LICENSE.LGPL LGPL_EXCEPTION.txt

%files -n qtscriptbindings-qt5-doc
%defattr(-,root,root,-)
%doc doc/
%doc examples/


%files -n qtscriptbindings-qt5-core
%{_qt5_plugindir}/script/libqtscript_core.so*

%files -n qtscriptbindings-qt5-gui
%{_qt5_plugindir}/script/libqtscript_gui.so*

%files -n qtscriptbindings-qt5-network
%{_qt5_plugindir}/script/libqtscript_network.so*

%files -n qtscriptbindings-qt5-opengl
%{_qt5_plugindir}/script/libqtscript_opengl.so*

%files -n qtscriptbindings-qt5-sql
%{_qt5_plugindir}/script/libqtscript_sql.so*

%files -n qtscriptbindings-qt5-svg
%{_qt5_plugindir}/script/libqtscript_svg.so*

%files -n qtscriptbindings-qt5-uitools
%{_qt5_plugindir}/script/libqtscript_uitools.so*

%files -n qtscriptbindings-qt5-webkit
%{_qt5_plugindir}/script/libqtscript_webkit.so*

%files -n qtscriptbindings-qt5-xml
%{_qt5_plugindir}/script/libqtscript_xml.so*

%files -n qtscriptbindings-qt5-xmlpatterns
%{_qt5_plugindir}/script/libqtscript_xmlpatterns.so*
