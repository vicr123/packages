Name:           theSlate
Version:        1.0
Release:        1%{?dist}
Summary:        Text Editor

License:        GPLv3+
URL:            https://github.com/vicr123/theslate
Source0:        https://github.com/vicr123/theSlate/archive/v%{version}.tar.gz

BuildRequires:  make qt5-devel qt5-qtwebengine-devel the-libs-devel kf5-syntax-highlighting-devel git
Requires:       qt5 qt5-qtwebengine the-libs kf5-syntax-highlighting

%define debug_package %{nil}
%define _unpackaged_files_terminate_build 0

%description
Text Editor

%prep
%setup

%build
git clone https://github.com/markedjs/marked.git AuxiliaryPanes/MarkdownPreview/marked
git --git-dir AuxiliaryPanes/MarkdownPreview/marked/.git --work-tree AuxiliaryPanes/MarkdownPreview/marked checkout c938aa1
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
%{_bindir}/theslate
%{_datadir}/theslate/*
%{_datadir}/applications/theslate.desktop
%{_datadir}/icons/hicolor/scalable/apps/theslate.svg


%changelog
* Sun May  3 2020 Victor Tran
- 
