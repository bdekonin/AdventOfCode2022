/* ************************************************************************** */
/*                                                                            */
/*                                                        ::::::::            */
/*   Elf.hpp                                            :+:    :+:            */
/*                                                     +:+                    */
/*   By: bdekonin <bdekonin@student.codam.nl>         +#+                     */
/*                                                   +#+                      */
/*   Created: 2022/12/01 15:45:37 by bdekonin      #+#    #+#                 */
/*   Updated: 2022/12/01 16:09:18 by bdekonin      ########   odam.nl         */
/*                                                                            */
/* ************************************************************************** */

#ifndef ELF_HPP
# define ELF_HPP

# include <iostream>
# include <string>

class Elf
{
	public:
		/* Constructor  */
		Elf()
		: _calories(0)
		{
			// std::cout << "Elf constructor called" << std::endl;
		}

		/* Destructor */
		virtual ~Elf()
		{
			// std::cout << "Elf destructor called" << std::endl;
		}

		// Methods
		void appendCalories(int calories)
		{
			this->_calories += calories;
		}

		const int getCalories() const
		{
			return this->_calories;
		}


	private:
		int _calories;
};

#endif // ELF_HPP