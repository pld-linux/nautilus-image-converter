Summary:	Nautilus extension to mass resize or rotate images
Summary(pl.UTF-8):	Rozszerzenie Nautilusa pozwalające masowo zmieniać rozmiar i obracać pliki graficzne
Name:		nautilus-image-converter
Version:	0.2.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://www.bitron.ch/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	e34708641777938bf76f1e3a3f062aee
URL:		http://www.bitron.ch/software/nautilus-image-converter.php
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gnome-desktop-devel >= 2.10.0
BuildRequires:	intltool >= 0.18
BuildRequires:	ImageMagick-devel
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.6.0
BuildRequires:	pkgconfig
Requires:	gnome-terminal
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus extension which allows you to mass resize or rotate images.

%description -l pl.UTF-8
Rozszerzenie Nautilusa pozwalające masowo zmieniać rozdzielczość i
obracać pliki graficzne.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/*.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/nautilus-image-*.glade
