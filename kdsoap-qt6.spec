%define		qtver		6.6.1
%define		kfname	kdsoap

Summary:	Qt-based client-side and server-side SOAP component
Name:		kdsoap-qt6
Version:	2.2.0
Release:	1
License:	LGPL v2.1, LGPL v3.0, GPL v2.0, GPL v3.0, commercial
Group:		X11/Libraries
Source0:	https://github.com/KDAB/KDSoap/releases/download/%{kfname}-%{version}/%{kfname}-%{version}.tar.gz
# Source0-md5:	a4ef201402aaa1500439a2ed4359c0f3
URL:		https://www.kdab.com/development-resources/qt-tools/kd-soap/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	Qt6Xml-devel >= %{qtver}
BuildRequires:	cmake >= 3.20.0
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KD Soap is a Qt-based client-side and server-side SOAP component.

%description -l pl.UTF-8
KD Soap jest opartym na Qt komponentem SOAP do programów po stronie
klienta jak i serwera.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cmake >= 3.5
Requires:	kf6-kconfig-devel >= %{version}
Requires:	kf6-kcoreaddons-devel >= %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKDSoap_QT6=ON
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSES README.md kdsoap.pri kdwsdl2cpp.pri
%attr(755,root,root) %{_bindir}/kdwsdl2cpp-qt6
%ghost %{_libdir}/libkdsoap-qt6.so.2
%attr(755,root,root) %{_libdir}/libkdsoap-qt6.so.*.*
%ghost %{_libdir}/libkdsoap-server-qt6.so.2
%attr(755,root,root) %{_libdir}/libkdsoap-server-qt6.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KDSoapClient-Qt6
%{_includedir}/KDSoapServer-Qt6
%{_libdir}/cmake/KDSoap-qt6
%{_libdir}/libkdsoap-qt6.so
%{_libdir}/libkdsoap-server-qt6.so
%dir %{_libdir}/qt6/mkspecs
%dir %{_libdir}/qt6/mkspecs/modules
%{_libdir}/qt6/mkspecs/modules/qt_KDSoapClient.pri
%{_libdir}/qt6/mkspecs/modules/qt_KDSoapServer.pri
