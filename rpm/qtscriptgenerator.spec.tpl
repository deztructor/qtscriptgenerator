
Name:    qtscriptgenerator@@suffix@@
Summary: A tool to generate Qt bindings for Qt Script
Version: 0.2.4
Release: 2

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
@@deps@@

%define my_qt_ver %{_qt@@ver@@_version}

# not strictly required, but the expectation would be for the
# bindings to be present
Requires: qtscriptbindings@@suffix@@-common = %{version}-%{release}

%description
Qt Script Generator is a tool to generate Qt bindings for Qt Script.

%package -n qtscriptbindings@@suffix@@-common
Summary: Qt bindings for Qt Script - common files
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings@@suffix@@-common
Common files for QtScript Qt bindings packages.

%package -n qtscriptbindings@@suffix@@-doc
Summary: Qt bindings for Qt Script - documentation and examples
Group: System Environment/Libraries
%{?_qt:Requires: qt%{?_isa} >= %{my_qt_ver}}
%description -n qtscriptbindings@@suffix@@-doc
Examples and documentation for QtScript Qt bindings

@@pkgs@@

%prep
%setup -q -n %{name}-%{version}

%build

# workaround buildsys bogosity, see also:
# http://code.google.com/p/qtscriptgenerator/issues/detail?id=38
export INCLUDE=/usr/include

export QTDIR=%{_qt@@ver@@_headerdir}

pushd generator
%qmake@@ver@@
make %{?jobs:-j%jobs}
./generator --include-paths=%{_qt@@ver@@_headerdir}
popd

pushd qtbindings
%qmake@@ver@@
make %{?jobs:-j%jobs}
popd

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_qt@@ver@@_plugindir}/script/
# install doesn't do symlinks
cp -a plugins/script/libqtscript* \
  %{buildroot}%{_qt@@ver@@_plugindir}/script/

install -D -p -m755 generator/generator %{buildroot}%{_qt@@ver@@_bindir}/qtbindings-generator

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_qt@@ver@@_bindir}/qtbindings-generator

%files -n qtscriptbindings@@suffix@@-common
%defattr(-,root,root,-)
%doc README
%doc LICENSE.LGPL LGPL_EXCEPTION.txt

%files -n qtscriptbindings@@suffix@@-doc
%defattr(-,root,root,-)
%doc doc/
%doc examples/

@@files@@
