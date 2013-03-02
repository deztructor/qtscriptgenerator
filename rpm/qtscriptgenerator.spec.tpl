
Name:    qtscriptgenerator
Summary: A tool to generate Qt bindings for Qt Script
Version: 0.2.4
Release: 2

License: GPLv2
Group:	 System Environment/Libraries
URL:     http://github.com/deztructor/qtscriptgenerator
Source0: qtscriptgenerator-%{version}.tar.bz2
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Patch0: qtscriptgenerator-src-0.1.0-qmake_target.path.patch
Patch1: qtscriptgenerator-0.2.0-arm-ftbfs-float.patch

# explictly BR libxslt, for xsltproc
BuildRequires: libxslt
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

# not strictly required, but the expectation would be for the
# bindings to be present
Requires: qtscriptbindings = %{version}-%{release}

%description
Qt Script Generator is a tool to generate Qt bindings for Qt Script.

%package -n qtscriptbindings-common
Summary: Qt bindings for Qt Script - common files
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{_qt_version}}
%description -n qtscriptbindings-common
Common files for QtScript Qt bindings packages.

%package -n qtscriptbindings-doc
Summary: Qt bindings for Qt Script - documentation and examples
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{_qt_version}}
%description -n qtscriptbindings-doc
Examples and documentation for QtScript Qt bindings

@@pkgs@@

%prep
%setup -q -n %{name}-%{version}

%patch0 -p1 -b .qmake_target.path

%ifarch %{arm}
%patch1 -p1 -b .arm_ftbfs_float
%endif

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

%files -n qtscriptbindings-common
%defattr(-,root,root,-)
%doc README
%doc LICENSE.LGPL LGPL_EXCEPTION.txt

%files -n qtscriptbindings-doc
%defattr(-,root,root,-)
%doc doc/
%doc examples/

@@files@@
