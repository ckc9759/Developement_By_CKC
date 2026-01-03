### Spring

---

IOC container

- Inversion of control
- contains objects
- Application context is used to acheive IOC container
- uses Annotaion to decide which objects to store in container, `@Component`
- `@Container` - Class is automatically registered as a Spring Bean (Object). 

- `Annotation` -> can be used on classes, interface, method, field. (information)
- `@SpringBootApplication` -> used for main class, `@Configuration`, `@EnableAutoConfiguration`, `@ComponentScan`.
- `@Autowired` -> Dependency Injection. Use some other class object in another class which is not null. Used to avoid new instances everytime if used in multiple class.

Eg. 
```java
Dog dog = new dog(); ->

@Autowired
private Dog dog;
# No need of creating new objects everytime.
```

---  

ORM = A technique used to map java objects in db tables. (Object Relational Mapping)
JPA = Java Persistence API, a way to acheive ORM. Includes interfaces and annotations. To use JPA, we need a persistence provider (ORM tool)
`Spring data JPA` - It simplifies working with JPA by providing higher level abstraction and utilities.

- JPA is not used with MongoDB, JPA is used mostly with RDBMS.
- MongoDB - nosql db
- ORM tools -> Hibernate, EclipseLink, OpenJPA





