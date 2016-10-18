Name:		qterminal
Version:	0.7.0
Release:	1%{?dist}
Summary:	A lightweight Qt5 terminal emulator
License:	GPLv2
URL:		https://github.com/qterminal/qterminal
Source0:	https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch0:     %{name}-fedberry-defaults.patch

BuildRequires:	desktop-file-utils
BuildRequires:  cmake
BuildRequires:	libqxt-devel
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  git
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(qtermwidget5) >= 0.7.0
BuildRequires:  pkgconfig(lxqt)

Conflicts:      qterminal-common
Conflicts:      qterminal-qt5
Obsoletes:      qterminal-common
Obsoletes:      qterminal-qt5

%description
QTerminal is a lightweight Qt5 terminal emulator based on QTermWidget.


%prep
%autosetup -p1


%build
%cmake -DUSE_QT5=ON -DUSE_SYSTEM_QXT=OFF
make %{?_smp_mflags}


%install
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}_drop.desktop
%find_lang %{name} --with-qt --without-mo


%post
%desktop_database_post


%postun
%desktop_database_postun


%files -f %{name}.lang
%license LICENSE
%doc AUTHORS CHANGELOG CONTRIBUTING.md README.md
%{_bindir}/%{name}
%{_datadir}/appdata/qterminal.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}_drop.desktop
%{_datadir}/icons/hicolor/64x64/apps/qterminal.png


%changelog
* Mon Oct 17 2016 Vaughan <devel at agrez.net> - 0.7.0-1
- New release
- Depreciate Qt4 build (drop separte qt5 / common rpms)
- Update BuildRequires/Conflicts/Obsoletes
- Update Patch0
- Use %autosetup
- Update Summary / Description
- Update %license %doc

* Mon Sep 19 2016 Vaughan <devel at agrez.net> - 0.6.0-6
- Update qterminal defaults

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 2 2015 TI_Eugene <ti.eugene@gmail.com> - 0.6.0-4
- Qt5 version added

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 10 2015 TI_Eugene <ti.eugene@gmail.com> - 0.6.0-2
- Rebuild with new qtermwidget

* Tue Nov 04 2014 TI_Eugene <ti.eugene@gmail.com> - 0.6.0-1
- Version bump

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-5
- Next git snapshot
- Changelog dates (year) fixed

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-3
- Source URL update
- second desktop validate added

* Mon May 06 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-2
- Source URL update

* Mon May 06 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-1
- initial packaging for Fedora
