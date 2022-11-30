#!/usr/bin/node

exports.converter = function (base) {
  function tobase (number) {
    return (number.toString(base));
  }
  return (tobase);
};
