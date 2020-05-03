Name:           theBeat
Version:        2.0.1
Release:        1%{?dist}
Summary:        Music Player

License:        GPLv3+
URL:            https://github.com/vicr123/thebeat
Source0:        https://github.com/vicr123/theBeat/archive/v%{version}.tar.gz

BuildRequires:  make qt5-devel the-libs-devel phonon-qt5-devel taglib-devel
Requires:       qt5 the-libs phonon-qt5 taglib

%define debug_package %{nil}
%define _unpackaged_files_terminate_build 0

%description
Music Player

%prep
%setup

%build
qmake-qt5
make

%install
rm -rf $RPM_BUILD_ROOT
#%make_install
make install INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%{_bindir}/thebeat
%{_datadir}/applications/thebeat.desktop
%{_datadir}/icons/thebeat.svg


%changelog
* Sun May  3 2020 Victor Tran
- 
