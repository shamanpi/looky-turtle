;; Auto-generated. Do not edit!


(when (boundp 'obj_tracker::strNum)
  (if (not (find-package "OBJ_TRACKER"))
    (make-package "OBJ_TRACKER"))
  (shadow 'strNum (find-package "OBJ_TRACKER")))
(unless (find-package "OBJ_TRACKER::STRNUM")
  (make-package "OBJ_TRACKER::STRNUM"))

(in-package "ROS")
;;//! \htmlinclude strNum.msg.html


(defclass obj_tracker::strNum
  :super ros::object
  :slots (_some_string _some_int ))

(defmethod obj_tracker::strNum
  (:init
   (&key
    ((:some_string __some_string) "")
    ((:some_int __some_int) 0)
    )
   (send-super :init)
   (setq _some_string (string __some_string))
   (setq _some_int (round __some_int))
   self)
  (:some_string
   (&optional __some_string)
   (if __some_string (setq _some_string __some_string)) _some_string)
  (:some_int
   (&optional __some_int)
   (if __some_int (setq _some_int __some_int)) _some_int)
  (:serialization-length
   ()
   (+
    ;; string _some_string
    4 (length _some_string)
    ;; uint32 _some_int
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _some_string
       (write-long (length _some_string) s) (princ _some_string s)
     ;; uint32 _some_int
       (write-long _some_int s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _some_string
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _some_string (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; uint32 _some_int
     (setq _some_int (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get obj_tracker::strNum :md5sum-) "f96250af5e3163f91ec8bac6b3aa2d91")
(setf (get obj_tracker::strNum :datatype-) "obj_tracker/strNum")
(setf (get obj_tracker::strNum :definition-)
      "string some_string
uint32 some_int

")



(provide :obj_tracker/strNum "f96250af5e3163f91ec8bac6b3aa2d91")


