### Springboot

---

Springboot is a framework for building apps in java.

Core spring already reduces boilerplate code and provides lots of features for java, springboot reduces the effort needed to setup and configure the apps.

[Playlist](https://www.youtube.com/watch?v=1993zSY5UBI&list=PLA3GkZPtsafacdBLdd3p1DyRd5FGfr3Ue&index=1)

- Auto configurations
- Standalone applications

No need to create an application annotation context. Eg. `@SpringBootApplication` annotation.

A bean can be declared once and can be used anywhere in the codebase.

#### Structure 

- `.idea` - intellij specific files
- `.mvn` - maven wrapper to run jar
- `gitignore` - ignore some files and directories for commit
- `src` - 

1. main -> java -> code , resources -> properties
2. test -> unit tests for the code in main

- `pom.xml` - how to build, external libraries, dependencies. parent tag -> inherits required dependencies, plugins etc.
- `FAT jar` - jar with bytecode, all dependencies as a self-contained jar which can be run directly without any external source.
---



