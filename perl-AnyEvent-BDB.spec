#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	AnyEvent
%define		pnam	BDB
Summary:	AnyEvent::BDB - truly asynchronous Berkeley DB access
Summary(pl.UTF-8):	AnyEvent::BDB - naprawdę asynchroniczny dostęp do Berkeley DB
Name:		perl-AnyEvent-BDB
Version:	1.1
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/ML/MLEHMANN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f9328fd98ced3bc078cdfbebcd3e16a4
URL:		http://search.cpan.org/dist/AnyEvent-BDB/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-AnyEvent >= 3.81
BuildRequires:	perl-BDB >= 1.5
%endif
Requires:	perl-AnyEvent >= 3.81
Requires:	perl-BDB >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AnyEvent::BDB is a module for truly asynchronous Berkeley DB access.

%description -l pl.UTF-8
AnyEvent::BDB to moduł udostępniający naprawdę asynchroniczny dostęp
do baz Berkeley DB.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/AnyEvent/BDB.pm
%{_mandir}/man3/AnyEvent::BDB.3pm*
