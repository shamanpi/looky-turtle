// Auto-generated. Do not edit!

// (in-package obj_tracker.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class strNum {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.some_string = null;
      this.some_int = null;
    }
    else {
      if (initObj.hasOwnProperty('some_string')) {
        this.some_string = initObj.some_string
      }
      else {
        this.some_string = '';
      }
      if (initObj.hasOwnProperty('some_int')) {
        this.some_int = initObj.some_int
      }
      else {
        this.some_int = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type strNum
    // Serialize message field [some_string]
    bufferOffset = _serializer.string(obj.some_string, buffer, bufferOffset);
    // Serialize message field [some_int]
    bufferOffset = _serializer.uint32(obj.some_int, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type strNum
    let len;
    let data = new strNum(null);
    // Deserialize message field [some_string]
    data.some_string = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [some_int]
    data.some_int = _deserializer.uint32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.some_string.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'obj_tracker/strNum';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f96250af5e3163f91ec8bac6b3aa2d91';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string some_string
    uint32 some_int
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new strNum(null);
    if (msg.some_string !== undefined) {
      resolved.some_string = msg.some_string;
    }
    else {
      resolved.some_string = ''
    }

    if (msg.some_int !== undefined) {
      resolved.some_int = msg.some_int;
    }
    else {
      resolved.some_int = 0
    }

    return resolved;
    }
};

module.exports = strNum;
