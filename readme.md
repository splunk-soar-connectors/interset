[comment]: # "Auto-generated SOAR connector documentation"
# Interset AI

Publisher: Interset  
Connector Version: 1\.0\.0  
Product Vendor: Interset  
Product Name: Interset  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.0\.1068  

This app allows integration with the Interset analytics platform by implementing contain and investigate actions pertaining to importance and risk details respectively

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Interset asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**server\_url** |  required  | string | Server URl for interset reporting ex\. 'http\://application\.ad\.interset\.com/' 
**auth\_token** |  required  | password | Authorization token of a user with persisten sessions and admin permissions\. ex 'aB3CdEfGHIJkl0MniyHAZndA44A'
**tid** |  required  | string | Tenant ID
**entityId** |  required  | string | Entity Id of the workflow user

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity  
[put importance](#action-put-importance) - Set the importance value of an entity  
[put user importance](#action-put-user-importance) - Set the importance value of a user  
[put project importance](#action-put-project-importance) - Set the importance value of a project  
[put file importance](#action-put-file-importance) - Set the importance value of a file  
[put device importance](#action-put-device-importance) - Set the importance value of a device  
[get importance](#action-get-importance) - Get the importance value of an entity  
[get user importance](#action-get-user-importance) - Get the importance value of a user  
[get file importance](#action-get-file-importance) - Get the importance value of a file  
[get device importance](#action-get-device-importance) - Get the importance value of a device  
[get project importance](#action-get-project-importance) - Get the importance value of a project  
[get risk](#action-get-risk) - Get an entity's risk value as determined by Interset analytics  
[get user risk](#action-get-user-risk) - Get a user's risk value as determined by Interset analytics  
[get file risk](#action-get-file-risk) - Get a file's risk value as determined by Interset analytics  
[get device risk](#action-get-device-risk) - Get a device's risk value as determined by Interset analytics  
[get project risk](#action-get-project-risk) - Get a project's risk value as determined by Interset analytics  

## action: 'test connectivity'
Validate the asset configuration for connectivity

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'put importance'
Set the importance value of an entity

Type: **contain**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**entityType** |  required  | The EntityType of the user whose risk you wish to get | string | 
**value** |  required  | Importance value | string | 
**entityId** |  required  | The EntityId of the user whose importance is being set | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.entityId | string | 
action\_result\.parameter\.entityType | string | 
action\_result\.parameter\.value | string | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'put user importance'
Set the importance value of a user

Type: **contain**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**value** |  required  | Importance value | string | 
**entityId** |  required  | The EntityId of the user whose importance is being set | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.entityId | string | 
action\_result\.parameter\.value | string | 
action\_result\.data\.\*\.value | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'put project importance'
Set the importance value of a project

Type: **contain**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**value** |  required  | Importance value | string | 
**entityId** |  required  | The EntityId of the project whose importance is being set | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.entityId | string | 
action\_result\.parameter\.value | string | 
action\_result\.data\.\*\.value | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'put file importance'
Set the importance value of a file

Type: **contain**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**value** |  required  | Importance value | string | 
**entityId** |  required  | The EntityId of the file whose importance is being set\. Please note this refers to the 'fileId' field of the endpoint schema and not the 'fileIdName'' | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.entityId | string | 
action\_result\.parameter\.value | string | 
action\_result\.data\.\*\.value | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'put device importance'
Set the importance value of a device

Type: **contain**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**value** |  required  | Importance value | string | 
**entityId** |  required  | The EntityId of the device whose importance is being set | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.entityId | string | 
action\_result\.parameter\.value | string | 
action\_result\.data\.\*\.value | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get importance'
Get the importance value of an entity

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**entityType** |  required  | The EntityType of the entity whose risk you wish to get | string | 
**entityId** |  required  | The EntityId of the entity you wish to get | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.entityId | string | 
action\_result\.parameter\.entityType | string | 
action\_result\.data\.\*\.value | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get user importance'
Get the importance value of a user

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**entityId** |  required  | The EntityId of the user you wish to get | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.entityId | string | 
action\_result\.data\.\*\.value | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get file importance'
Get the importance value of a file

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**entityId** |  required  | The EntityId of the file you wish to get\. Please note this refers to the 'fileId' field of the endpoint schema and not the 'fileIdName'' | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.entityId | string | 
action\_result\.data\.\*\.value | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get device importance'
Get the importance value of a device

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**entityId** |  required  | The EntityId of the device you wish to get | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.entityId | string | 
action\_result\.data\.\*\.value | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get project importance'
Get the importance value of a project

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**entityId** |  required  | The EntityId of the project you wish to get | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.entityId | string | 
action\_result\.data\.\*\.value | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get risk'
Get an entity's risk value as determined by Interset analytics

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**entityType** |  required  | The EntityType of the entity whose risk you wish to get | string | 
**entityId** |  required  | The EntityId of the entity whose risk you wish to get | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.entityId | string | 
action\_result\.parameter\.entityType | string | 
action\_result\.data\.\*\.data\.0\.score | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get user risk'
Get a user's risk value as determined by Interset analytics

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**entityId** |  required  | The EntityId of the user whose risk you wish to get | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.entityId | string | 
action\_result\.data\.\*\.data\.0\.score | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get file risk'
Get a file's risk value as determined by Interset analytics

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**entityId** |  required  | The EntityId of the file whose risk you wish to get\. Please note this refers to the 'fileId' field of the endpoint schema and not the 'fileIdName' | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.entityId | string | 
action\_result\.data\.\*\.data\.0\.score | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get device risk'
Get a device's risk value as determined by Interset analytics

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**entityId** |  required  | The EntityId of the device whose risk you wish to get | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.entityId | string | 
action\_result\.data\.\*\.data\.0\.score | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get project risk'
Get a project's risk value as determined by Interset analytics

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**entityId** |  required  | The EntityId of the project whose risk you wish to get | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.entityId | string | 
action\_result\.data\.\*\.data\.0\.score | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 