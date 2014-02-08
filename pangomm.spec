%define api_version 2.4
%define realapi 1.4
%define major 1
%define libname %mklibname %{name} %{api_version} %{major}
%define libnamedev %mklibname -d %{name} %{api_version}
%define libnamestaticdev %mklibname -d -s %{name} %{api_version}

Name:		pangomm
Summary:	C++ interface for the pango library
Version:	2.28.4
Release:	6
License:	LGPLv2+
Group:		System/Libraries
URL:		http://gtkmm.org/
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source100:	pangomm.rpmlintrc
BuildRequires:	pkgconfig(mm-common-util)
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(cairomm-1.0)
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
Provides:	%{name}%{api_version} = %{version}-%{release}

%description	-n %{libname}
Gtkmm provides a C++ interface to the GTK+ GUI library. Gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains the library needed to run programs dynamically
linked with %{name}.

%package	-n %{libnamedev}
Summary:	Headers and development files of %{name}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}%{api_version}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description	-n %{libnamedev}
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
%configure2_5x \
    --enable-static \
    --enable-shared \
    --disable-static
%make

# make check does nothing

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%{_libdir}/libpangomm-%{realapi}.so.%{major}*

%files -n %{libnamedev}
%doc COPYING ChangeLog AUTHORS COPYING NEWS README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/pangomm-%{realapi}/

%files doc
%doc %{_datadir}/doc/pangomm-%{realapi}/
%doc %{_datadir}/devhelp/books/*


%changelog
* Mon Apr 16 2012 Götz Waschk <waschk@mandriva.org> 2.28.4-4
+ Revision: 791322
- rebuild

* Fri Mar 16 2012 Andrey Bondrov <abondrov@mandriva.org> 2.28.4-3
+ Revision: 785292
- Rebuild with new RPM dependency generator

  + Zé <ze@mandriva.org>
    - add missing buildrequire pangocairo
    - buildrequires pkg usage

* Tue Dec 06 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.28.4-2
+ Revision: 738040
- added correct BR pkgconfig(pangocairo)

  + Zé <ze@mandriva.org>
    - fix pango build require
    - clean defattr, BR, clean setion and mkrel
    - move doc to devel
    - clean static files
    - clena .la files
    - clean useless macros

* Wed Oct 26 2011 Götz Waschk <waschk@mandriva.org> 2.28.4-1
+ Revision: 707303
- update to new version 2.28.4

* Tue Sep 27 2011 Götz Waschk <waschk@mandriva.org> 2.28.3-1
+ Revision: 701449
- update to new version 2.28.3

* Mon Sep 19 2011 Götz Waschk <waschk@mandriva.org> 2.28.2-4
+ Revision: 700375
- rebuild

* Mon Sep 19 2011 Götz Waschk <waschk@mandriva.org> 2.28.2-3
+ Revision: 700318
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.28.2-2
+ Revision: 666986
- mass rebuild

* Wed Mar 30 2011 Götz Waschk <waschk@mandriva.org> 2.28.2-1
+ Revision: 649062
- update to new version 2.28.2

* Fri Mar 25 2011 Götz Waschk <waschk@mandriva.org> 2.28.1-1
+ Revision: 648476
- update to new version 2.28.1

* Wed Mar 23 2011 Götz Waschk <waschk@mandriva.org> 2.28.0-1
+ Revision: 648033
- update build deps
- update to new version 2.28.0

* Fri Dec 10 2010 Götz Waschk <waschk@mandriva.org> 2.26.3-2mdv2011.0
+ Revision: 620434
- rebuild
- update to new version 2.26.3

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.26.2-2mdv2011.0
+ Revision: 607069
- rebuild

* Tue May 04 2010 Götz Waschk <waschk@mandriva.org> 2.26.2-1mdv2010.1
+ Revision: 541982
- update to new version 2.26.2

* Fri Apr 16 2010 Götz Waschk <waschk@mandriva.org> 2.26.1-1mdv2010.1
+ Revision: 535419
- update to new version 2.26.1

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.26.0-2mdv2010.1
+ Revision: 523591
- rebuilt for 2010.1

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2010.0
+ Revision: 446584
- update to new version 2.26.0

* Sat Aug 29 2009 Götz Waschk <waschk@mandriva.org> 2.25.1.3-1mdv2010.0
+ Revision: 422127
- update to new version 2.25.1.3

* Fri Aug 28 2009 Götz Waschk <waschk@mandriva.org> 2.25.1.1-1mdv2010.0
+ Revision: 422005
- update to new version 2.25.1.1

* Wed Aug 26 2009 Götz Waschk <waschk@mandriva.org> 2.25.1-1mdv2010.0
+ Revision: 421434
- update to new version 2.25.1

* Tue Mar 10 2009 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.1
+ Revision: 353433
- new version

* Mon Nov 10 2008 Götz Waschk <waschk@mandriva.org> 2.14.1-1mdv2009.1
+ Revision: 301802
- update to new version 2.14.1

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 2.14.0-1mdv2009.0
+ Revision: 286525
- new version

* Wed Sep 10 2008 Götz Waschk <waschk@mandriva.org> 2.13.8-1mdv2009.0
+ Revision: 283467
- new version

* Mon Aug 04 2008 Götz Waschk <waschk@mandriva.org> 2.13.7-1mdv2009.0
+ Revision: 263290
- new version
- fix directory version

* Sun Jul 27 2008 Götz Waschk <waschk@mandriva.org> 2.13.6-1mdv2009.0
+ Revision: 250616
- new version

* Wed Jul 23 2008 Götz Waschk <waschk@mandriva.org> 2.13.5-1mdv2009.0
+ Revision: 242423
- update file list
- import pangomm


