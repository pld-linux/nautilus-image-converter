Summary:	Nautilus extension to mass resize or rotate images
Summary(pl.UTF-8):	Rozszerzenie Nautilusa pozwalające masowo zmieniać rozmiar i obracać pliki graficzne
Name:		nautilus-image-converter
Version:	0.3.0
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-image-converter/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	1eb9343c285281354bc9dbf81f566b5a
URL:		http://www.bitron.ch/software/nautilus-image-converter.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.1
BuildRequires:	gtk+2-devel >= 2:2.12.8
BuildRequires:	intltool >= 0.37.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.22.0
BuildRequires:	pkgconfig
Requires:	ImageMagick
Requires:	nautilus >= 2.22.0
Suggests:	ImageMagick-coder-jpeg
Suggests:	ImageMagick-coder-jpeg2
Suggests:	ImageMagick-coder-png
Suggests:	ImageMagick-coder-tiff
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus extension which allows you to mass resize or rotate images.

%description -l pl.UTF-8
Rozszerzenie Nautilusa pozwalające masowo zmieniać rozdzielczość i
obracać pliki graficzne.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/libnautilus-image-converter.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/nautilus-image-resize.glade
%{_datadir}/%{name}/nautilus-image-rotate.glade
