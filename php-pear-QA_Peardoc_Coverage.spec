%include	/usr/lib/rpm/macros.php
%define		_class		QA
%define		_subclass	Peardoc_Coverage
%define		_status		stable
%define		_pearname	QA_Peardoc_Coverage
Summary:	%{_pearname} - PEAR documentation coverage analysis
Summary(pl.UTF-8):	%{_pearname} - analiza pokrycia kodu przez dokumentację PEAR
Name:		php-pear-%{_pearname}
Version:	1.1.1
Release:	3
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	feb3b9e4d0c3f761f00651aa9e2e1937
URL:		http://pear.php.net/package/QA_Peardoc_Coverage/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-QA_Peardoc_Coverage-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Takes the PEAR documentation CVS and the PEAR package CVS directories,
and compares which packages have been documented. Also checks which
classes and methods have been documented, and generates HTML reports.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten pobiera z CVS dokumentację oraz klasy PEAR, a następnie
sprawdza które pakiety i w jakim stopniu zostały udokumentowane. Z
przeprowadzonej analizy jest następnie generowany raport HTML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/QA_Peardoc_Coverage/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/QA/Peardoc
%{php_pear_dir}/QA/Peardoc/Coverage.php
