#!/usr/bin/node

/**
 * esrever - Reverses the elements of a list.
 * @list: The list to be reversed.
 *
 * Return: The reversed list.
 */
exports.esrever = function(list) {
	const reversedList = [];

	for (let i = list.length - 1; i >= 0; i--) {
		reversedList.push(list[i]);
	}

	return reversedList;
};
