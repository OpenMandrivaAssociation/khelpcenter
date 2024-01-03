%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name: khelpcenter
Version:	23.08.4
Release:	2
# was part of plasma but moved to applications in 16.04
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE Plasma 5 Help Center
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(xapian-core)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Bookmarks)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Init)
BuildRequires: cmake(KF5KHtml)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(Grantlee5)
Conflicts:	kde-runtime < 1:15.04.3-3

%description
KDE Plasma 5 Help Center.

%prep
%setup -qn %{name}-%{version}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang khelpcenter5 || touch khelpcenter5.lang

%files -f khelpcenter5.lang
%{_datadir}/qlogging-categories5/khelpcenter.categories
%{_bindir}/khelpcenter
%{_libdir}/libexec/*
%{_datadir}/metainfo/*.xml
%{_datadir}/applications/org.kde.khelpcenter.desktop
%{_datadir}/dbus-1/services/org.kde.khelpcenter.service
%{_datadir}/config.kcfg/khelpcenter.kcfg
%{_datadir}/khelpcenter
%{_datadir}/kservices5/khelpcenter.desktop
%{_datadir}/kde4/services/khelpcenter.desktop
%doc %{_docdir}/HTML/*/fundamentals
%doc %{_docdir}/HTML/*/khelpcenter
%doc %{_docdir}/HTML/*/onlinehelp
