%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: khelpcenter
Version: 5.1.95
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: KDE Plasma 5 Help Center
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5Init)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5KHtml)
BuildRequires: cmake(KF5KDE4Support)
BuildRequires: ninja

%description
KDE Plasma 5 Help Center

%prep
%setup -qn %{name}-%{plasmaver}
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}
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
%doc %{_docdir}/HTML/en/fundamentals
%doc %{_docdir}/HTML/en/khelpcenter
%doc %{_docdir}/HTML/en/onlinehelp
