%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	1.4
%define major	1
%define libname	%mklibname %{name} %{api} %{major}
%define devname	%mklibname -d %{name}
%define _disable_rebuild_configure 1

Summary:	C++ interface for the pango library
Name:		pangomm
Version:	2.40.1
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		http://gtkmm.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pangomm/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(cairomm-1.0)
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(mm-common-util)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)

%description
Pangomm provides a C++ interface to the Pango library. Highlights
include typesafe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%package	-n %{libname}
Summary:	C++ interface for the pango library
Group:		System/Libraries
Obsoletes:	%{_lib}pangomm2.4_1 < 2.28.4-7

%description	-n %{libname}
Gtkmm provides a C++ interface to the GTK+ GUI library. Gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains the library needed to run programs dynamically
linked with %{name}.

%package	-n %{devname}
Summary:	Headers and development files of %{name}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}pangomm2.4-devel < 2.28.4-7

%description	-n %{devname}
This package contains the headers and development files that are needed,
when trying to develop or compile applications which need %{name}.

%package	doc
Summary:	GTKmm documentation
Group:		Books/Other

%description	doc
Pangomm provides a C++ interface to the Pango library. Highlights
include typesafe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains all API documentation for pangomm. You can readily read
this documentation with devhelp, a documentation reader.

%prep
%setup -q

%build
%configure \
	--enable-shared \
	--disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libpangomm-%{api}.so.%{major}*

%files -n %{devname}
%doc COPYING ChangeLog AUTHORS COPYING NEWS README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/pangomm-%{api}/
%doc %{_datadir}/doc/pangomm-%{api}/
%doc %{_datadir}/devhelp/books/*

