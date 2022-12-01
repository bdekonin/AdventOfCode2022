/* ************************************************************************** */
/*                                                                            */
/*                                                        ::::::::            */
/*   main.cpp                                           :+:    :+:            */
/*                                                     +:+                    */
/*   By: bdekonin <bdekonin@student.codam.nl>         +#+                     */
/*                                                   +#+                      */
/*   Created: 2022/12/01 15:50:24 by bdekonin      #+#    #+#                 */
/*   Updated: 2022/12/01 16:19:43 by bdekonin      ########   odam.nl         */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

#include "Elf.hpp"

int main(int argc, char **argv)
{
	/* Read from file */
	std::ifstream file;
	file.open("input.txt");
	if (!file.is_open())
	{
		std::cout << "Error: file not found" << std::endl;
		return (1);
	}
	std::string line;
	std::vector<std::string> lines;
	while (std::getline(file, line))
		lines.push_back(line);

	/* Create Elves */
	std::vector<Elf*> elves;

	for (int i = 0; i < lines.size(); i++)
	{
		/* Line is empty find next elf */
		while (i < lines.size() && lines[i].empty())
			i++;
		
		if (i >= lines.size())
			break;

		/* Line is not empty, create elf */
		Elf *elf = new Elf();

		/* Add calories to elf */

		while (i < lines.size() && !lines[i].empty())
		{
			elf->appendCalories(std::stoi(lines[i]));
			i++;
		}

		/* Add elf to vector */
		elves.push_back(elf);
	}
	/* Error checking*/
	if (elves.size() == 0)
	{
		std::cout << "Error: no elves found" << std::endl;
		return (1);
	}

	/* Calculate total calories */
	Elf *biggestElf = nullptr;
	biggestElf = elves[0];
	if (elves.size() > 1)
	{
		for (int i = 0; i < elves.size(); i++)
		{
			if (elves[i]->getCalories() > biggestElf->getCalories())
				biggestElf = elves[i];
		}
	}
	
	/* Print total calories */
	std::cout << "The elf carrying the most has " << biggestElf->getCalories() << " calories" << std::endl;

	/* Free Memory */
	for (int i = 0; i < elves.size(); i++)
		delete elves[i];
	return (0);
}