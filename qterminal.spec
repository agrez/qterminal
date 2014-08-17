%global commit 57a11b193dabbd0fce988c5e196077cf732172dd
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		qterminal
Version:	0.4.0
Release:	7%{?dist}
License:	GPLv2
Source0:	https://github.com/qterminal/qterminal/tarball/%{commit}/%{name}-%{name}-%{version}-%{shortcommit}.tar.gz
Summary:	Advanced terminal emulator
URL:		https://github.com/qterminal/qterminal
BuildRequires:	cmake, pkgconfig(QtGui), qtermwidget-devel >= 0.4.0-6, libqxt-devel, desktop-file-utils

%description
Advanced terminal emulator with many useful bells and whistles.

%prep
%setup -qn %{name}-%{name}-%{shortcommit}
rm -rf src/third-party

%build
mkdir build
pushd build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo ..
make %{?_smp_mflags}
popd

%install
pushd build
%make_install
popd
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}_drop.desktop
%find_lang %{name} --with-qt --without-mo

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
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
