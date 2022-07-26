Name:           disomaster
Version:        5.0.7
Release:        1
Summary:        Library to manipulate DISC burning
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{name}_%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  libisoburn-devel

%description
This package provides a libisoburn wrapper class for Qt.


%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?isa}
Requires:       libisoburn-devel%{?isa}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q
sed -i 's|/lib|/%{_lib}|' lib%{name}/lib%{name}.pro

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.1*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Jul 26 2022 liweiganga <liweiganga@uniontech.com> - 5.0.7-1
- update to 5.0.7

* Fri Aug 7 2020 weidong <weidong@uniontech.com> - 5.0.1-1
- Initial release for OpenEuler
