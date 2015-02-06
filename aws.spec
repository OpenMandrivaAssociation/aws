%define name    aws
%define version 1.75
%define release 2

# Source tar.bz is created by downloading script from
# http://timkay.com/aws
# (https://raw.github.com/timkay/aws/master/aws)

Summary:	Command line access to Amazon S3, EC2 and SQS
Name:		%{name}
Version:	%{version}
Release: 	%{release}	
License:	GPLv3
Group:		Networking/Other
URL:		http://timkay.com/aws/
Source0:	%{name}-%{version}.tar.bz
Requires:	curl
BuildArch: 	noarch
BuildRoot:	%{_tmppath}/%{name}-root

%description
aws is a command line tool that gives you easy access to 
Amazon EC2, S3 and SQS.  aws is designed to be simple to
install and simple to use.

aws S3 (Simple Storage Service) allows you to create 
buckets/directories, add and remove files and list buckets.  

aws EC2 (Elastic Compute Cloud) allows you to start, 
stop, reboot, and manage EC2 virtual machines.

aws SQS (Simple Queue Service) is used to control queues. 

%prep

%setup -q

%build

%install
rm -fr %{buildroot}
install -m 755 -D aws %{buildroot}/%{_bindir}/aws
install -m 644 -D README %{buildroot}/%{_docdir}/aws/README

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%doc README 
%{_bindir}/aws




%changelog
* Sun Jan 08 2012 Glen Ogilvie <nelg@mandriva.org> 1.75-1mdv2012.0
+ Revision: 758647
- New release: 1.75

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.39-2mdv2011.0
+ Revision: 616673
- the mass rebuild of 2010.0 packages

* Thu May 28 2009 Glen Ogilvie <nelg@mandriva.org> 1.39-1mdv2010.0
+ Revision: 380306
- tidy up of spec file based on feedback
- updated packager
- import aws


* Fri May 01 2009 Glen Ogilvie <nelg@linuxsolutions.co.nz> 1.39-1mdv2009.1
+ RPM build from source
