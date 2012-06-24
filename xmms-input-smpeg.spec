Summary:	MPEG video playing plugin for xmms
Summary(pl):	Wtyczka odtwarzaj�ca filmy MPEG dla xmms
Name:		xmms-input-smpeg
Version:	0.3.5
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.xmms.org/files/plugins/smpeg-xmms/smpeg-xmms-%{version}.tar.gz
Patch0:		%{name}-am15.patch
Requires:	xmms
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	smpeg-devel
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	xmms-smpeg
Obsoletes:	smpeg-xmms


%description
This plugin allows xmms to play MPEG movies.

%description -l pl
Ta wtyczka pozwala xmms'owi odtwarza� filmy w formacie MPEG.

%prep
%setup -q -n smpeg-xmms-%{version}
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
CPPFLAGS="-L%{_libdir}"; export CPPFLAGS
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO NEWS README ChangeLog
%attr(755,root,root) %{_libdir}/xmms/Input/*
