%global _minos_commit f1a31721ed7f43f38240e801e2d2b6b0d56fc342
%global _vpath_srcdir minos-%{_minos_commit}

Name:           minos
Version:        0.0.16
Release:        1%{?dist}
Summary:        Minos daemon and NSS module

License:        BSD
URL:            https://github.com/afq984/minos
Source:         %{url}/archive/%{_minos_commit}.zip

BuildRequires: gcc                                                                                                                                            
BuildRequires: pkgconfig(glib-2.0)                                                                                                                            
BuildRequires: pkgconfig(libzmq)                                                                                                                              
BuildRequires: meson                                                                                                                                          

%description
%{summary}.

%prep
%autosetup -c

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%{_bindir}/minos-*
%{_libdir}/libnss_minos.so*
%{_prefix}/lib/systemd/system/minos-*.service
%{_sysconfdir}/minos.d/*.conf

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
