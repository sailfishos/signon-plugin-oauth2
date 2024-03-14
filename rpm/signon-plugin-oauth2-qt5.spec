Name: signon-plugin-oauth2-qt5
Version: 0.25
Release: 0
Summary: Plugin which provides oauth and oauth2 authentication enablers to signond
License: LGPLv2
URL: https://github.com/sailfishos/signon-plugin-oauth2
Source0: %{name}-%{version}.tar.bz2
Patch0: 0001-Manually-time-out-HTTP-requests-after-30-seconds.patch
Patch1: 0002-OAuth2-Relax-RefreshToken-restriction-on-ProvidedTok.patch
Patch2: 0003-Always-install-to-usr-lib-never-usr-lib64.patch
Patch3: 0004-Always-force-client-auth-via-request-body.patch
Patch4: 0005-Support-Microsoft-OAuth2-flow.patch
Patch5: 0006-Add-ExtraParams-to-plugin-data.patch
Patch6: 0007-Add-RFC7636-aka-PKCE-support.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(signond)


%description
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}/signon-plugin-oauth2

%package oauthclient
Summary: OAuth2 SignOn Plugin OAuth Client

%description oauthclient
%{summary}.

%package devel
Summary: Tests for the oauth2 signon plugin

%description devel
%{summary}.

%package tests
Summary: Tests for the oauth2 signon plugin

%description tests
%{summary}.

%build
%qmake5 CONFIG+=make_examples
make %{?_smp_mflags}

%install
%qmake5_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/signon/liboauth2plugin.so
%license COPYING

%files oauthclient
%{_bindir}/oauthclient
%{_sysconfdir}/signon-ui/webkit-options.d/m.facebook.com.conf
%{_sysconfdir}/signon-ui/webkit-options.d/www.facebook.com.conf

%files devel
%{_includedir}/signon-plugins/oauth1data.h
%{_includedir}/signon-plugins/oauth2data.h
%{_libdir}/pkgconfig/signon-oauth2plugin.pc

%files tests
%{_bindir}/signon-oauth2plugin-tests
%{_datadir}/signon-oauth2plugin-tests/tests.xml
