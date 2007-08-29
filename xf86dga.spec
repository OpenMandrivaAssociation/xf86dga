Name: xf86dga
Version: 1.0.1
Release: %mkrel 7
Summary: Test program for the XFree86
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Patch0: xf86dga-1.0.1-use-xaw8.patch
# check setuid return value in order to guarantee dropping user privilegies
Patch1: http://xorg.freedesktop.org/releases/X11R7.1/patches/xf86dga-1.0.1-setuid.diff
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: libxmu-devel >= 1.0.0
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxxf86dga-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: autoconf

%description
Dga is a simple test client for the XFree86-DGA extension. It fills the screen
with a different colour for each key pressed. It prints some basic framebuffer
parameters, and also keyboard and pointer events to stdout. 

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .xaw8
%patch1 -p0 -b .setuid

rm -f configure && autoconf

%build
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
%{_mandir}/man1/dga.1x*


