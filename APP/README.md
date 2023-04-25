# ** Chapter 02 **
<br><br>

## **Overview of Understanding**
<br><br>

| Concept | Understanding | Questions | Notes |
| --- | --- | --- | --- |
| ORM Depends on Model | Goal: to remove dependency of Domain on ORM, instead, have ORM depend on Domain | Curious as to model.Orderline not having ID defined in the class in model.py | |
| Test_ORM | Goal: Testing loading and saving | orderid is set to "order1" which is string, not autoincremented Integer | Discovered model.py needs frozen=True to be unsafe_hash=True / Also updating for |
|Repository| Goal: to run without actually touching a database, instead, holds in memory | Not confident in understanding alchemy repo, assuming calling session as if it was a database? Or is this following conftest.py?  | Had to downgrade SQLAlchemy |
| Test_Repo | Saving a batch straight forward | Allocations more complicated and more confusing as it takes allocate from batch, however allocations is still somewhat confusing. Is it always allocations? or does that come from model? | |
<br><br>

## **Helpful Links**
* Unsafe_Hash - https://github.com/cosmicpython/code/issues/17
* SQLAlchemy Depreciated Mapper - https://github.com/cosmicpython/code/issues/41

## **Notes**
* Working currently with SQLAlchemy 2.0.X versions implemented.
* Must pass engine that was created within conftest.py and use the .begin() to open the connection, plus new parameters include having text(SQL STATMENTS) within the executes.
* After struggling with concepts around moving repository to SQLALchemy 2.0, I dropped back to 1.4

