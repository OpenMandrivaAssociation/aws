%define name    aws
%define version 1.39
%define release %mkrel 2

Summary:	Command line access to Amazon S3, EC2 and SQS
Name:		%{name}
Version:	%{version}
Release: 	%{release}	
License:	GPLv3
Group:		Networking/Other
URL:		http://timkay.com/aws/
Packager:	Glen Ogilvie <nelg@mandriva.org>
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

%setup

%build

%install
rm -fr $RPM_BUILD_ROOT
install -m 755 -D aws $RPM_BUILD_ROOT/%{_bindir}/aws
install -m 644 -D README $RPM_BUILD_ROOT/%{_docdir}/aws/README

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README 
%{_bindir}/aws


