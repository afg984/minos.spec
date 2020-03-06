%global _minos_commit 6afc0ce5f374271f4fb774547622712401bf2ee9
%global _vpath_srcdir minos-%{_minos_commit}

Name:           minos
Version:        0.0.21
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
