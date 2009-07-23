%define upstream_name    prefork
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Optimize module loading across forking and non-forking scenarios
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl(Scalar::Util) >= 1.10
BuildRequires:	perl-ExtUtils-AutoInstall >= 0.49
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Provides:   perl(prefork)

%description
The prefork pragma is intended to allow module writers to optimise
module loading for both scenarios with as little additional code as
possible.

The prefork.pm is intended to serve as a central and optional
marshalling point for state detection (are we running in procedural or
pre-forking mode) and to act as a relatively light-weight module loader.

Loaders and Forkers
prefork is intended to be used in two different ways.

The first is by a module that wants to indicate that another module
should be loaded before forking. This is known as a "Loader".

The other is a script or module that will be initiating the forking. It
will tell prefork.pm that it is either going to fork, or is about to
fork, and that the modules previously mentioned by the Loaders should be
loaded immediately.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/prefork.pm
%{_mandir}/*/*


