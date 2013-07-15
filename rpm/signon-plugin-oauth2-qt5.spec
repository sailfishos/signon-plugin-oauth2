Name: signon-plugin-oauth2-qt5
Version: 0.15
Release: 1
Summary: Plugin which provides oauth and oauth2 authentication enablers to signond
Group: System/Libraries
License: LGPLv2.1
URL: http://code.google.com/p/accounts-sso/
Source: %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(libsignon-qt5)

%description
%{summary}.

%files
%defattr(-,root,root,-)
%{_libdir}/signon/liboauth2plugin.so

%prep
%setup -n %{name}-%{version}/%{name}

%package -n signon-plugin-oauth2-qt5-oauthclient
Summary: OAuth2 SignOn Plugin OAuth Client
Group: System/Tools

%description -n signon-plugin-oauth2-qt5-oauthclient
%{summary}.

%files -n signon-plugin-oauth2-qt5-oauthclient
%defattr(-,root,root,-)
%{_bindir}/oauthclient
%{_includedir}/signon-plugins/oauth1data.h
%{_includedir}/signon-plugins/oauth2data.h
%{_libdir}/pkgconfig/signon-oauth2plugin.pc
%{_sysconfdir}/signon-ui/webkit-options.d/m.facebook.com.conf
%{_sysconfdir}/signon-ui/webkit-options.d/www.facebook.com.conf

%package -n signon-plugin-oauth2-qt5-tests
Summary: Tests for the oauth2 signon plugin
Group: System/Libraries

%description -n signon-plugin-oauth2-qt5-tests
%{summary}.

%files -n signon-plugin-oauth2-qt5-tests
%{_bindir}/signon-oauth2plugin-tests
%{_datadir}/signon-oauth2plugin-tests/tests.xml

%build
%qmake5
make %{?jobs:-j%jobs}

%install
%qmake5_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
