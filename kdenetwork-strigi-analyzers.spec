Summary:	KDE network strigi plugins
Name:		kdenetwork-strigi-analyzers
Version:	4.11.0
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libstreamanalyzer)

%description
This package provides:
- Strigi meta information plugin for BitTorrent files (*.torrent).

%files
%{_kde_libdir}/strigi/strigita_torrent_analyzer.so

#-------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.0-1
- New version 4.11.0
- Split from kdenetwork4 package as upstream did

