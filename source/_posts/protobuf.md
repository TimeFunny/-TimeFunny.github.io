---
title: protobuf
date: 2019-08-27 14:40:54
tags:
 - protocol buffer

---

<!-- toc -->

### a  message type

- field types

  ```
  string query
  int32 page_numbe
  ```

- field numbers

  ​    each field in the message definition has a **unique number**. These field numbers are used to identify your fields in the [message binary format](https://developers.google.cn/protocol-buffers/docs/encoding), and should not be changed once your message type is in use.

  

- field rules

  - singular: a well-formed message can have zero or one of this field(default)

  - repeated: this field can be repeated any number of times (including zero) in a well-formed message.

```
/* SearchRequest represents a search query, with pagination options to
 * indicate which results to include in the response. */

message SearchRequest {
  string query = 1;
  int32 page_number = 2;  // Which page number do we want?
  int32 result_per_page = 3;  // Number of results to return per page.
}
```

### Reserved Fields

```
message Foo {
  reserved 2, 15, 9 to 11;
  reserved "foo", "bar";
}
```





### Importing Definitions

```
import "myproject/other_protos.proto";
```

**Move a `.proto` file to a new location**

```
// new.proto
// All definitions are moved here

// old.proto
// This is the proto that all clients are importing.
import public "new.proto";
import "other.proto";

// client.proto
import "old.proto";
// You use definitions from old.proto and new.proto, but not other.proto
```

### Packages

You can add an optional `package` specifier to a `.proto` file to prevent name clashes between protocol message types.

```
package foo.bar;
message Open { ... }
```

You can then use the package specifier when defining fields of your message type:

```
message Foo {
  ...
  foo.bar.Open open = 1;
  ...
}
```



[Reference](https://developers.google.cn/protocol-buffers/docs/proto3)