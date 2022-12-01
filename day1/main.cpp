/* ************************************************************************** */
/*                                                                            */
/*                                                        ::::::::            */
/*   main.cpp                                           :+:    :+:            */
/*                                                     +:+                    */
/*   By: bdekonin <bdekonin@student.codam.nl>         +#+                     */
/*                                                   +#+                      */
/*   Created: 2022/12/01 15:50:24 by bdekonin      #+#    #+#                 */
/*   Updated: 2022/12/01 16:34:58 by bdekonin      ########   odam.nl         */
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
	else if (elves.size() == 1)
	{
		std::cout << "Error: only one elf found" << std::endl;
		return (1);
	}

	std::sort(elves.begin(), elves.end(), [](Elf *a, Elf *b) { return a->getCalories() > b->getCalories(); });

	/* Print elves */
	for (int i = 0; i < elves.size(); i++)
	{
		std::cout << "Elf " << i + 1 << " has " << elves[i]->getCalories() << " calories" << std::endl;
	}

	/* Print awnsers */
	std::cout << "Part One: " << elves[0]->getCalories() << std::endl;
	std::cout << "Part Two: " << elves[0]->getCalories() + elves[1]->getCalories() + elves[2]->getCalories() << std::endl;
	
	/* Print total calories */
	// std::cout << "The elf carrying the most has " << biggestElf->getCalories() << " calories" << std::endl;

	/* Free Memory */
	for (int i = 0; i < elves.size(); i++)
		delete elves[i];
	return (0);
}
