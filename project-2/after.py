"""
Very advanced Employee management system.
"""

from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterable, List

FIXED_VACATION_DAYS_PAYOUT = (
    5  # The fixed no. of vacation days that can be paid out.
)


class RoleEnum(Enum):
    INTERN = "INTERN"
    MANAGER = "MANAGER"
    VICE_PRESIDENT = "VISE_PRESIDENT"
    PRESIDENT = "PRESIDENT"


@dataclass
class Employee:
    """Basic representation of an employee at the company."""

    name: str
    role: RoleEnum
    vacation_days: int = 25

    def take_a_holiday(self):
        if self.vacation_days < 1:
            raise ValueError(
                "You don't have any holidays left. Now back to work, you!"
            )
        self.vacation_days -= 1
        print("Have fun on your holiday. Don't forget to check your emails!")

    def payout_a_holiday(self):
        # check that there are enough vacation days left for a payout
        if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            raise ValueError(
                f"You don't have enough holidays left over for a payout.\
                    Remaining holidays: {self.vacation_days}."
            )
        try:
            self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
            print(f"Paying out a holiday. Holidays left: {self.vacation_days}")
        except Exception:
            # this should never happen
            pass

    @abstractmethod
    def accept_payment(self):
        raise NotImplementedError


@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""

    hourly_rate: float = 50
    amount: int = 10

    def accept_payment(self):
        print(
            f"Paying employee {self.name} a hourly rate of \
                ${self.hourly_rate} for {self.amount} hours."
        )


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""

    monthly_salary: float = 5000

    def accept_payment(self):
        print(
            f"Paying employee {self.name} a monthly "
            f"salary of ${self.monthly_salary}."
        )


class Company:
    """Represents a company with employees."""

    def __init__(self) -> None:
        self.employees: Dict[RoleEnum, List[Employee]] = {}

    def __iter__(self) -> Iterable[Employee]:
        for _, employees in self.employees.items():
            for employee in employees:
                yield employee

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the list of employees."""
        existing_employees = self.employees.get(employee.role, [])
        existing_employees.append(employee)
        self.employees[employee.role] = existing_employees

    def find_managers(self) -> List[Employee]:
        """Find all manager employees."""
        return self.employees.get(RoleEnum.MANAGER, [])

    def find_vice_presidents(self) -> List[Employee]:
        """Find all vice-president employees."""
        return self.employees.get(RoleEnum.VICE_PRESIDENT, [])

    def find_interns(self) -> List[Employee]:
        """Find all interns."""
        return self.employees.get(RoleEnum.INTERN, [])

    def pay_employee(self, employee: Employee) -> None:
        """Pay an employee."""
        return employee.accept_payment()


def main() -> None:
    """Main function."""

    company = Company()
    manager = SalariedEmployee(name="Louis", role=RoleEnum.MANAGER)
    president = HourlyEmployee(name="Brenda", role=RoleEnum.PRESIDENT)
    intern = HourlyEmployee(name="Tim", role=RoleEnum.INTERN)

    company.add_employee(manager)
    company.add_employee(president)
    company.add_employee(intern)

    print(company.find_vice_presidents())
    print(company.find_managers())
    print(company.find_interns())

    company.pay_employee(manager)
    manager.take_a_holiday()


if __name__ == "__main__":
    main()
