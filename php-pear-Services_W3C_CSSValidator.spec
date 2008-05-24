%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	W3C_CSSValidator
%define		_status		alpha
%define		_pearname	Services_W3C_CSSValidator
Summary:	%{_pearname} - An Object Oriented Interface to the W3C CSS Validator service
Summary(pl.UTF-8):	%{_pearname} - zorientowany obiektowo interfejs do usługi walidacji CSS
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	3
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7d4caa54880de5b94808db8cba85f665
URL:		http://pear.php.net/package/Services_W3C_CSSValidator/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTTP_Request >= 1.3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an object oriented interface to the API of the
W3 CSS Validator application (http://jigsaw.w3.org/css-validator/).
With this package you can connect to a running instance of the
validator and retrieve the validation results (true|false) as well as
the errors and warnings for a a style sheet.

By using the SOAP 1.2 output format from the validator, you are
returned simple objects containing all the information from the
validator.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten udostępnia zorientowanego obiektowo interfejsu do API
usługi kontroli poprawności CSS serwisu W3C
(http://jigsaw.w3.org/css-validator/). Przy użyciu tego pakietu
możliwe jest podłączenie się do instancji walidatora i pobranie wyniku
kontroli poprawności (prawda|fałsz) jak również komunikatów błędów i
ostrzeżeń dla danego arkusza stylów.

Poprzez wykorzystanie formatu SOAP 1.2, w wyniku zwracane są proste
obiekty zawierające wszystkie informacje walidatora.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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
%doc install.log
%doc docs/Services_W3C_CSSValidator/docs/examples
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/Services/W3C
%{php_pear_dir}/Services/W3C/CSSValidator
%{php_pear_dir}/Services/W3C/CSSValidator.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Services_W3C_CSSValidator
