Summary:	MPEG video playing plugin for xmms
Summary(pl):	Wtyczka odtwarzaj±ca filmy MPEG dla xmms
Name:		xmms-input-smpeg
Version:	0.3.2
Release:	2
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
License:	GPL
Source0:	http://www.xmms.org/files/plugins/smpeg-xmms/smpeg-xmms-%{version}.tar.gz
Requires:	xmms
BuildRequires:	xmms-devel
BuildRequires:	libstdc++-devel
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	SDL-devel
BuildRequires:	smpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This plugin allows xmms to play MPEG movies.

%description -l pl
Ta wtyczka pozwala xmms'owi odtwarzaæ filmy w formacie MPEG

%prep
%setup -q -n smpeg-xmms-%{version}

%build
autoheader;autoconf;automake; 
export CPPFLAGS="-L%{_libdir}"
%configure 

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS TODO NEWS README ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/xmms/Input/*
