Name: signon-plugin-oauth2
Version: 0.15
Release: 1
Summary: Plugin which provides oauth and oauth2 authentication enablers to signond
Group: System/Libraries
License: LGPLv2.1
URL: http://code.google.com/p/accounts-sso/
Source: %{name}-%{version}.tar.bz2
Patch0: 0001-Manually-time-out-HTTP-requests-after-30-seconds.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: pkgconfig(signond)
BuildRequires: pkgconfig(QJson)
BuildRequires: pkgconfig(QtCore)
BuildRequires: pkgconfig(signon-plugins)

%description
%{summary}.

%files
%defattr(-,root,root,-)
%{_libdir}/signon/liboauth2plugin.so

%prep
%setup -n %{name}-%{version}/%{name}

%patch0 -p1

%package -n signon-plugin-oauth2-oauthclient
Summary: OAuth2 SignOn Plugin OAuth Client
Group: System/Tools

%description -n signon-plugin-oauth2-oauthclient
%{summary}.

%files -n signon-plugin-oauth2-oauthclient
%defattr(-,root,root,-)
%{_bindir}/oauthclient
%{_includedir}/signon-plugins/oauth1data.h
%{_includedir}/signon-plugins/oauth2data.h
%{_libdir}/pkgconfig/signon-oauth2plugin.pc
%{_sysconfdir}/signon-ui/webkit-options.d/m.facebook.com.conf
%{_sysconfdir}/signon-ui/webkit-options.d/www.facebook.com.conf

%package -n signon-plugin-oauth2-tests
Summary: Tests for the oauth2 signon plugin
Group: System/Libraries

%description -n signon-plugin-oauth2-tests
%{summary}.

%files -n signon-plugin-oauth2-tests
%{_bindir}/signon-oauth2plugin-tests
%{_datadir}/signon-oauth2plugin-tests/tests.xml

%build
%qmake
make %{?jobs:-j%jobs}

%install
%qmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
