Name: icex-themes
Version: 0.0.1
Release: alt1

Summary: Themes for icex
Group: Graphical desktop/Icewm
License: GPL
Url: https://www.github.com/150balbes/icex-themes.git
Packager: Oleg Ivanov <Leo-sp150@yandex.ru>

Requires: icex

Source0: themes.tar

BuildArch: noarch
%description
Themes for icex

%prep
%build
%install
mkdir -p %buildroot%_datadir/icewm/themes
tar xf %SOURCE0 -C %buildroot%_datadir/icewm/

%files
%dir %_datadir/icewm/themes
%_datadir/icewm/*

%changelog
* Sun Feb 27 2016 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt1
- init version
