Name:		xf86dga
Version:	1.0.2
Release:	%mkrel 3
Summary:	Test program for the XFree86-DGA extension
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	libx11-devel >= 1.0.0
BuildRequires:	libxxf86dga-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	autoconf

Patch4: 0004-xf86dga-doesn-t-need-xaw-xt-and-xmu-libraries.patch

%description
Dga is a simple test client for the XFree86-DGA extension. It fills the screen
with a different colour for each key pressed. It prints some basic framebuffer
parameters, and also keyboard and pointer events to stdout. 

%prep
%setup -q -n %{name}-%{version}

%patch4 -p1

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
