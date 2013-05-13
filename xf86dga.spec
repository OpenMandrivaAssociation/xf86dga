Name:		xf86dga
Version:	1.0.3
Release:	%mkrel 2
Summary:	Test program for the XFree86-DGA extension
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xxf86dga) >= 1.1.0
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	autoconf

%description
Dga is a simple test client for the XFree86-DGA extension. It fills the screen
with a different colour for each key pressed. It prints some basic framebuffer
parameters, and also keyboard and pointer events to stdout. 

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -ifs
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/dga
%{_mandir}/man1/dga.1*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2011.0
+ Revision: 671307
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 592597
- drop patch 4 (merged upstream)
- new release
- bump BR on libxxf86dga-devel

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-5mdv2010.1
+ Revision: 524439
- rebuilt for 2010.1

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-4mdv2009.0
+ Revision: 226034
- rebuild

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-3mdv2008.1
+ Revision: 166517
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-2mdv2008.1
+ Revision: 154782
- xf86dga package doesn't need xaw, xt and xmu.
  Update accordingly.
- Updated BuildRequires and resubmit package.
- Patch not required
- This is a program to test the dga interface, and doesn't require xaw, xt or xmu

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.2-1mdv2008.0
+ Revision: 76523
- rebuild for 2008
- fix manpage filename
- drop patch1 (merged upstream)
- new release 1.0.2
- minor spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - do not hardcode lzma extension!!!


* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 14:46:34 (59319)
- bumping release

* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 14:35:26 (59313)
- fix typos in previous commit

* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 01:21:27 (59273)
- bumping release

* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 01:08:49 (59271)
- Add a patch fixing setuid calls. The return value should be verified in order
  to assure the user privilegies were dropped. (#24976)

* Mon Aug 14 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-14 14:25:21 (55969)
- Use libxaw8 instead of old legacy library

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-30 20:38:46 (31751)
- rebuild against new libXaw package

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 23 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-23 22:24:58 (31400)
- fill in a couple of missing descriptions

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

