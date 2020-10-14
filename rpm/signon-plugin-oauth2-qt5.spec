Name: signon-plugin-oauth2-qt5
Version: 0.21.7
Release: 0
Summary: Plugin which provides oauth and oauth2 authentication enablers to signond
License: LGPLv2
URL: http://code.google.com/p/accounts-sso/
Source0: %{name}-%{version}.tar.bz2
Patch0: 0001-Manually-time-out-HTTP-requests-after-30-seconds.patch
Patch1: 0002-OAuth2-Relax-RefreshToken-restriction-on-ProvidedTok.patch
Patch2: 0003-Always-install-to-usr-lib-never-usr-lib64.patch
Patch3: 0004-Always-force-client-auth-via-request-body.patch
Patch4: 0005-Skip-unstable-unit-tests.patch
Patch5: 0006-Fix-dropbox-authentication-by-removing-type-query-ar.patch
Patch6: 0007-Support-OneDrive-oauth2-flow.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5Test)
# FIXME: change to pkgconfig(signond) when mer core no longer provides broken qt4-using
# signond.pc
BuildRequires: signon-qt5-devel


%description
%{summary}.

%files
%defattr(-,root,root,-)
%{_libdir}/signon/liboauth2plugin.so
%license COPYING

%prep
%setup -q -n %{name}-%{version}/signon-plugin-oauth2

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%package oauthclient
Summary: OAuth2 SignOn Plugin OAuth Client

%description oauthclient
%{summary}.

%files oauthclient
%defattr(-,root,root,-)
%{_bindir}/oauthclient
%{_sysconfdir}/signon-ui/webkit-options.d/m.facebook.com.conf
%{_sysconfdir}/signon-ui/webkit-options.d/www.facebook.com.conf


%package devel
Summary: Tests for the oauth2 signon plugin

%description devel
%{summary}.

%files devel
%{_includedir}/signon-plugins/oauth1data.h
%{_includedir}/signon-plugins/oauth2data.h
%{_libdir}/pkgconfig/signon-oauth2plugin.pc


%package tests
Summary: Tests for the oauth2 signon plugin

%description tests
%{summary}.

%files tests
%{_bindir}/signon-oauth2plugin-tests
%{_datadir}/signon-oauth2plugin-tests/tests.xml


%build
sed -i 's,$${INSTALL_PREFIX}/lib64,$${INSTALL_PREFIX}/lib,g' common-project-config.pri
%qmake5
make %{?jobs:-j%jobs}

%install
%qmake5_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
