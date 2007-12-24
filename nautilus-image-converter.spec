Summary:	Nautilus extension to mass resize or rotate images
Summary(pl.UTF-8):	Rozszerzenie Nautilusa pozwalające masowo zmieniać rozmiar i obracać pliki graficzne
Name:		nautilus-image-converter
Version:	0.2.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-image-converter/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	1759c4811944242b023a13da3fafc89c
URL:		http://www.bitron.ch/software/nautilus-image-converter.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs2-devel >= 2.6.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.6.0
BuildRequires:	pkgconfig
Requires:	ImageMagick
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
