import {
    Box,
    Text
} from "@chakra-ui/react"

export default function AnswerBox({ answer }) {
    return (
        <Box
            border={'2px solid green'}
            borderRadius={'0.25rem'}
            p={5}
            mt={3}
        >
            <Text>
                {answer}
            </Text>
        </Box>
    )
}