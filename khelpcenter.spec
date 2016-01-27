%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: khelpcenter
Version: 5.5.4
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: KDE Plasma 5 Help Center
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5Init)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5KHtml)
BuildRequires: cmake(KF5KDE4Support)
Conflicts:	kde-runtime < 1:15.04.3-3

%description
KDE Plasma 5 Help Center.

%prep
%setup -qn %{name}-%{plasmaver}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang khelpcenter
%find_lang htmlsearch
%find_lang kcmhtmlsearch
cat *.lang >all.lang

%files -f all.lang
%{_bindir}/khelpcenter
%{_libdir}/libexec/*
%{_libdir}/libkdeinit5_khelpcenter.so
%{_datadir}/applications/org.kde.Help.desktop
%{_datadir}/config.kcfg/khelpcenter.kcfg
%{_datadir}/dbus-1/interfaces/*
%{_datadir}/khelpcenter
%{_datadir}/kservices5/khelpcenter.desktop
%{_datadir}/kxmlgui5/khelpcenter
%{_datadir}/kde4/services/khelpcenter.desktop
%doc %{_docdir}/HTML/*/fundamentals
%doc %{_docdir}/HTML/*/khelpcenter
%doc %{_docdir}/HTML/*/onlinehelp
%doc %{_docdir}/HTML/*/glossary
