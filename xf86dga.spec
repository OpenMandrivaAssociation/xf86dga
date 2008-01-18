Name:		xf86dga
Version:	1.0.2
Release:	%mkrel 2
Summary:	Test program for the XFree86-DGA extension
Group:		Development/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/app/xf86dga xorg/app/xf86dga
# cd xorg/app/xf86dga
# git-archive --format=tar --prefix=xf86dga-1.0.2/ xf86dga-1.0.2 | bzip2 -9 > xf86dga-1.0.2.tar.bz2
########################################################################
Source:		%{name}-%{version}.tar.bz2
License:	MIT
########################################################################
# git-format-patch xf86dga-1.0.2..origin/mandriva
Patch1: 0001-Rename-.cvsignore-to-.gitignore.patch
Patch2: 0002-Add-to-.gitignore-to-skip-patch-emacs-droppings.patch
Patch3: 0003-Replace-static-ChangeLog-with-dist-hook-to-generate.patch
Patch4: 0004-xf86dga-doesn-t-need-xaw-xt-and-xmu-libraries.patch
########################################################################
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	x11-util-macros		>= 1.1.5
BuildRequires:	libx11-devel		>= 1.1.3
BuildRequires:	libxxf86dga-devel	>= 1.0.2

%description
Dga is a simple test client for the XFree86-DGA extension. It fills the screen
with a different colour for each key pressed. It prints some basic framebuffer
parameters, and also keyboard and pointer events to stdout. 

%prep
%setup -q -n %{name}-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
autoreconf -ifs
%configure	--x-includes=%{_includedir}\
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
