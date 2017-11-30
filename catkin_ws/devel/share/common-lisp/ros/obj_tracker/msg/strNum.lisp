; Auto-generated. Do not edit!


(cl:in-package obj_tracker-msg)


;//! \htmlinclude strNum.msg.html

(cl:defclass <strNum> (roslisp-msg-protocol:ros-message)
  ((some_string
    :reader some_string
    :initarg :some_string
    :type cl:string
    :initform "")
   (some_int
    :reader some_int
    :initarg :some_int
    :type cl:integer
    :initform 0))
)

(cl:defclass strNum (<strNum>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <strNum>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'strNum)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name obj_tracker-msg:<strNum> is deprecated: use obj_tracker-msg:strNum instead.")))

(cl:ensure-generic-function 'some_string-val :lambda-list '(m))
(cl:defmethod some_string-val ((m <strNum>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader obj_tracker-msg:some_string-val is deprecated.  Use obj_tracker-msg:some_string instead.")
  (some_string m))

(cl:ensure-generic-function 'some_int-val :lambda-list '(m))
(cl:defmethod some_int-val ((m <strNum>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader obj_tracker-msg:some_int-val is deprecated.  Use obj_tracker-msg:some_int instead.")
  (some_int m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <strNum>) ostream)
  "Serializes a message object of type '<strNum>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'some_string))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'some_string))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'some_int)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'some_int)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'some_int)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'some_int)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <strNum>) istream)
  "Deserializes a message object of type '<strNum>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'some_string) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'some_string) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'some_int)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'some_int)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'some_int)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'some_int)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<strNum>)))
  "Returns string type for a message object of type '<strNum>"
  "obj_tracker/strNum")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'strNum)))
  "Returns string type for a message object of type 'strNum"
  "obj_tracker/strNum")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<strNum>)))
  "Returns md5sum for a message object of type '<strNum>"
  "f96250af5e3163f91ec8bac6b3aa2d91")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'strNum)))
  "Returns md5sum for a message object of type 'strNum"
  "f96250af5e3163f91ec8bac6b3aa2d91")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<strNum>)))
  "Returns full string definition for message of type '<strNum>"
  (cl:format cl:nil "string some_string~%uint32 some_int~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'strNum)))
  "Returns full string definition for message of type 'strNum"
  (cl:format cl:nil "string some_string~%uint32 some_int~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <strNum>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'some_string))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <strNum>))
  "Converts a ROS message object to a list"
  (cl:list 'strNum
    (cl:cons ':some_string (some_string msg))
    (cl:cons ':some_int (some_int msg))
))
