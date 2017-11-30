
(cl:in-package :asdf)

(defsystem "obj_tracker-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "strNum" :depends-on ("_package_strNum"))
    (:file "_package_strNum" :depends-on ("_package"))
  ))